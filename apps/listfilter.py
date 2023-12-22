from django.template.library import Library
register = Library()
from django.template.defaulttags import register
@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg]


picture_list = [
    {
        'id' : 0,
        'author' : 'Anna',
        'title' : 'Sunset at the Beach',
        'price' : 59.99,
        'info' : "A beautiful oil painting capturing the warm colors of the sunset over a peaceful beach. The painting features a lone seagull flying in the distant sky, adding to the calming mood of the scene.",
        'date' : '26 July 2021',
        'address' : 'placeholder.png'
    },
    {
        'id' : 1,
        'author' : 'Barbara',
        'title' : 'The Red Tree',
        'price' : 49.99,
        'info' : "A striking acrylic painting that features a lone red tree amidst a lush green forest. The tree's bright red color draws the eye and adds a touch of mystery and intrigue to the otherwise peaceful landscape.",
        'date' : '01 January 2022',
        'address' : 'placeholder.png'
    },
    {
        'id' : 2,
        'author' : 'Chistopher',
        'title' : 'A Walk in the Rain',
        'price' : 69.99,
        'info' : "A watercolor painting depicting a couple walking in the rain. The vivid colors and soft strokes give the scene a dreamy quality, as though the viewer is watching the couple from a distance.",
        'date' : '11 September 2019',
        'address' : 'placeholder.png'
    },
    {
        'id' : 3,
        'author' : 'Daniel',
        'title' : 'Abstract Cityscape',
        'price' : 74.99,
        'info' : "An abstract painting that captures the energy and chaos of a cityscape. The bold colors and dynamic brushstrokes give a sense of movement and excitement, but also an underlying feeling of restlessness and uncertainty.",
        'date' : '29 July 2022',
        'address' : 'placeholder.png'
    },
    {
        'id' : 4,
        'author' : 'Eve',
        'title' : 'Portrait of a Woman',
        'price' : 124.99,
        'info' : "A stunning oil painting of a woman's portrait. The artist has captured the subject's piercing gaze and subtle expression with exquisite detail, conveying a sense of mystery and complexity. The vibrant yet subtle colors add to the painting's overall elegance and sophistication.",
        'date' : '15 April 2017',
        'address' : 'placeholder.png'
    },
]

def parse_list(dict):
    id_prefix = 'modal-card-'
    for item in dict:
        item['price'] = str(item['price'])
        item['id'] = id_prefix + str(item['id'])
        item['address'] = 'images/' + item['address']
    return dict
