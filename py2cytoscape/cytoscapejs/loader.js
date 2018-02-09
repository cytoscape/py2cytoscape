if (window['cytoscape'] === undefined) {
    var paths = {
        //seems like cystoscape.min.js has been relocated
        //from version 3.0.0 cytoscape.min.js does not work :(
        //cytoscape: 'http://cytoscape.github.io/cytoscape.js/api/cytoscape.js-latest/cytoscape.min'
        cytoscape: 'https://cdnjs.cloudflare.com/ajax/libs/cytoscape/2.7.21/cytoscape.min'
    };

    require.config({
        paths: paths
    });

    require(['cytoscape'], function (cytoscape) {
        console.log('Loading Cytoscape.js Module...');
        window['cytoscape'] = cytoscape;

        var event = document.createEvent("HTMLEvents");
        event.initEvent("load_cytoscape", true, false);
        window.dispatchEvent(event);
    });
}
