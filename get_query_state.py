from json import loads


def get_query_data(sesh, url):
    res = sesh.get(url)

    text_content = res
    
    start = text_content.index('queryState')

    map_bounds = text_content.index('"mapBounds":', start)
    end = text_content.index('}', map_bounds)

    location_data = text_content[map_bounds + len('"mapBounds":'):end + 1]
    location_data = loads(location_data)

    region_start = text_content.index('{"regionId"', start)
    region_end = text_content.index('}', region_start)

    region_data = text_content[region_start:region_end + 1]
    region_data = loads(region_data)

    return location_data, region_data