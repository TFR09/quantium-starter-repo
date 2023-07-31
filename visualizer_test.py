from visualize import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=5)
    assert len(dash_duo.find_element("h1")) == 1


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#pink_morsel_sale_graph", timeout=5)
    assert len(dash_duo.find_element("#pink_morsel_sale_graph")) == 1


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region", timeout=5)
    assert len(dash_duo.find_element("#region")) == 1
    