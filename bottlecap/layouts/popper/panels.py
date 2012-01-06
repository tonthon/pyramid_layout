from bottlecap.panel import panel_config

@panel_config(name='popper.global_logo',
              renderer='templates/global_logo.pt')
def global_logo(context, request):
    logo_href = request.registry.settings['bottlecap.site_title_link']
    logo_title = request.registry.settings['bottlecap.site_title']
    return dict(
        logo_href=logo_href,
        logo_title=logo_title,
    )

@panel_config(name='popper.global_nav',
        renderer='templates/global_nav.pt')
def global_nav(context, request):
    nav_menu = [
        dict(title="Item 1", url='#', selected=None),
        dict(title="Item 2", url='#', selected="selected"),
        dict(title="Item 3", url='#', selected=None),
        dict(title="Item 4", url='#', selected=None),
        dict(title="Item 5", url='#', selected=None)]
    return {'nav_menu': nav_menu}

@panel_config(name='popper.personal_tools',
              renderer='templates/personal_tools.pt')
def personal_tools(context, request):
    return dict(profile_name="John Doe")

@panel_config(name='popper.search', renderer='templates/search.pt')
@panel_config(name='popper.context_tools',
              renderer='templates/context_tools.pt')
@panel_config(name='popper.actions_menu', renderer='templates/actions_menu.pt')
@panel_config(name='popper.column_one', renderer='templates/column_one.pt')
def column_one(context, request):
    return {}