import poplib

from django.core.exceptions import ObjectDoesNotExist

from listapp.models import Category, Link


def _filter_content(lines):
    """Filters lines of email content.
    Returns only lines with content: subject and body lines."""
    for idx, line in enumerate(lines):
        if line.startswith('Subject: '):
            lines = lines[idx:]
            break
    else:
        # Subject line not found, discard
        return None
    # Grab subject from subject line
    # len('Subject: ') == 8
    subject = lines[0][8:]
    # Find empty line that starts email body
    for idx, line in enumerate(lines):
        if line == '':
            if len(lines) - 1 <= idx:
                return None
            lines = lines[idx + 1:]
            break
    else:
        return None
    # Filter empty lines
    lines = [l for l in lines if l]
    return [subject] + lines


def _parse_create_categories(cat_text):
    """Parses email line of categories.
    For each word, gets or creates categories using word as tag.
    Each new category has tag=word.lower() and name=word.title().
    Returns list of category objects.
    """
    categories = []
    cat_words = cat_text.split()
    for cat in cat_words:
        try:
            cat_obj = Category.objects.get(tag=cat.lower())
        except ObjectDoesNotExist:
            cat_obj = Category(name=cat.title(),
                               tag=cat.lower())
            cat_obj.save()
        categories.append(cat_obj)
    return categories


def _content_to_link(title, url='', comment='', categories='', *lines):
    """Uses content and creates a Link object."""
    link = Link(title=title)
    if url:
        link.url = url
    if comment:
        link.comment = comment
    link.save()
    categories = _parse_create_categories(categories)
    link.category.add(*categories)
    return link


def fetchmails(mailbox):
    """Fetches emails, sends each email text to parser functions.
    Deletes every email at the end."""
    M = poplib.POP3_SSL(mailbox.host)
    M.user(mailbox.username)
    M.pass_(mailbox.password)

    num_msgs = len(M.list()[1])
    num_links = 0

    for i in range(num_msgs):
        mail_lines = M.retr(i + 1)[1]
        data = _filter_content(mail_lines)
        if data is not None:
            # Link will be created.
            _content_to_link(*data)
            num_links += 1
        M.dele(i + 1)
    M.quit()
    return num_links
