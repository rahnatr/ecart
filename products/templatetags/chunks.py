from django import template

register=template.Library()

@register.filter(name='chunks')
def chunks(list_data,chunks_size):
    chunk=[]
    i=0
    if list_data is not None:
        for data in list_data:
            chunk.append(data)
            i=i+1
            if i==chunks_size:
                yield chunk
                i=0
                chunk=[]
        if chunk:
            yield chunk
    else:
        print("list_data is None")