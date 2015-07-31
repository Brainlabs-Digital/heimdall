var page = require('webpage').create(),
    system = require('system'),
    MAX_EXECUTION_TIME   = 30000,
    RENDER_AFTER = 7000,
    address, output_path, size_arr, user_agent;

if (system.args.length != 5) {
    console.log('FATAL: usage take_screenshot.js URL filename "0000px*0000px" "useragent"');
    phantom.exit(1);
} else {
    
    address = system.args[1];
    output_path = system.args[2];
    size_arr = system.args[3].split('*');
    user_agent = system.args[4];



    // Set our screen size
    pageWidth = parseInt(size_arr[0], 10);
    pageHeight = parseInt(size_arr[1], 10);
    page.viewportSize = { width: pageWidth, height: pageHeight };

    crop_to_visible = false;
    if (5 in system.args){
        crop_to_visible = system.args[5];
    }

    if (crop_to_visible) {
        page.clipRect = {
            top: 0,
            left: 0,
            width: pageWidth,
            height: pageHeight 
        }   
    }

    // Settings for page open
    page.settings.userAgent = user_agent    
    page.settings.resourceTimeout = 3000;

    console.log('Address: ' + address)
    console.log('Output Path: ' + output_path)
    console.log('Width: ' + pageWidth)
    console.log('Height: ' + pageHeight)
    console.log('UserAgent: ' + user_agent)
    if (crop_to_visible){
        console.log('clipRect: t:'
                + page.clipRect.top
                + ' l:'
                + page.clipRect.left
                + ' width:'
                + page.clipRect.width
                + ' height:'
                + page.clipRect.height
                )
    }


    // Add in some error handling
    page.onResourceError = function(resourceError) {
        page.reason = resourceError.errorString;
        page.reason_url = resourceError.url;
    };


    try {

        page.open(address, function (status) {
            if (status !== 'success') {
                console.log('Status: ' + status)
                console.log('Reason: ' + page.reason)
                console.log('Reason URL: ' + page.reason_url)

                phantom.exit();
            } else {

                //default the page background to white to avoid transparent issues
                //http://phantomjs.org/faq.html
                page.evaluate(function() {
                    document.body.bgColor = 'white';
                });

                window.setTimeout(function () {
                    var url = page.url
                    if(url != address){
                        console.log('REDIRECTED_TO: [' + url + ']')
                    }

                    page.render(output_path, {format: 'png', quality: '100'});
                
                    console.log('Status: SUCCESS')

                    phantom.exit();
                }, RENDER_AFTER);
            }
        });

    } finally {
        setTimeout(function() {
            console.log('Status: FAILED')
            console.log("Max execution time " + Math.round(MAX_EXECUTION_TIME) + " seconds exceeded");
            phantom.exit(1);
        }, MAX_EXECUTION_TIME);
    }
}