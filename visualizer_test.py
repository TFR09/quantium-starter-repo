from visualize import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1")


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#pink_morsel_sale_graph")


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region")
    