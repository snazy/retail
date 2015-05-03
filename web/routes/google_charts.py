from flask import Blueprint, render_template, request

gcharts_api = Blueprint('gcharts_api', __name__)


supported_charts = {
    'Table': 'table',
    'BarChart': 'corechart',
    'ColumnChart': 'corechart',
    'LineChart': 'corechart',
    'PieChart': 'corechart',
    'AreaChart': 'corechart'
}

def compose_ajax_source():
    """
    grab request GET variables to create new url
    :return: ajax ready url
    """
    # grab url parameter, if available
    url = request.args.get('url')

    # pass all other parameters to ajax url
    ajax_source = '%s?' % url
    for k, v in request.args.iteritems():
        if k not in ['url','options']:
            ajax_source += '&%s=%s' % (k, v)

    return ajax_source

#
# Render a basic flexible charts page
#   Parameters:
#      url=the url to return the chart data
#      options= google charting options
#        for more info see "customizing charts":
#          https://developers.google.com/chart/interactive/docs/customizing_charts
#          https://developers.google.com/chart/interactive/docs/datesandtimes#axesgridlinesticks
#

@gcharts_api.route('/<type>/')
def googlechart(type='ColumnChart'):
    ajax_source = compose_ajax_source()
    options = request.args.get('options',{})

    return render_template('google_charts.jinja2',
                           ajax_source=ajax_source,
                           chart_type=type,
                           package=supported_charts[type],
                           options=options)