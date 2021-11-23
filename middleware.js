const realFetch = fetch;
window.fetch = (url, args) => {
    if (url.indexOf('GetSearchPageCustomRegion.htm') != -1) {
        realFetch(url, args).then(e => e.json()).then(json => window.map_coords_return = json)
        console.log('draw fetch')
    }
    else
        console.log(0)
    return realFetch(url, args)
}
