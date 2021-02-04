from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone


register = template.Library()

TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """
TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                  <tr>
                    <td>{name}</td>
                    <td>{value}</td>
                  </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Діагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Частота процесора': 'processor_freq',
        "Оперативна пам'ять": 'ram',
        'Відеокарта': 'video',
        'Чаc автономної роботи': 'time_without_charge',
    },
    'smartphone': {
        'Діагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Розширення екрану': 'resolution',
        "Об'єм батареї": 'accum_volume',
        "Оперативна пам'ять": 'ram',
        "Слот для карт пам'яті": 'sd',
        "Максимальний об'єм карти пам'яті": 'sd_volume_max',
        'Головна камера (МП)': 'main_cam_mp',
        'Фронтальна камера (МП)': 'frontal_cam_mp',
    }
}
#не працює належним чином

def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop("Максимальний об'єм карти пам'яті")
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
