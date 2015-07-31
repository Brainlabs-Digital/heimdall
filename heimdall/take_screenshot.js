var system = require('system'),
    page = require('webpage').create(),
    optparse = require('./optparse');

// Set defaults
var args = {};
args.height = 420;
args.width = 300;
args.dir = '/tmp';
args.name = 'phantomimg';
args.ext = 'png';
args.quality = 100;
args.user_agent = 'heimdall';
args.crop_to_visible = false;
args.max_execution_time = 30000;
args.render_after = 7000;
args.resource_timeout = 3000;

var switches = [
    ['--help', 'Show the help'],
    ['-h', '--height NUMBER', 'Set the height, defaults to ' + args.height],
    ['-w', '--width NUMBER', 'Set the height, defaults to ' + args.width],
    ['-u', '--useragent', 'The useragent to set, defaults to ' + args.user_agent],
    ['-c', '--croptovisible', 'Include the whole webpage or just the visible bit, defaults to ' + args.crop_to_visible],    
    ['-d', '--dir', 'The folder to save to, defaults to ' + args.dir],
    ['-n', '--name', 'The name of the image to save, defaults to ' + args.name],
    ['-e', '--ext', 'The extension (and hence format) of the saved image, defaults to ' + args.ext],
    ['-q', '--quality', 'The quality of the image to save, defaults to ' + args.quality],
    ['-r', '--renderafter NUMBER', 'How many ms to wait before we render, defaults to ' + args.render_after],
    ['-m', '--maxexecutiontime NUMBER', 'How many ms to wait before we die, defaults to ' + args.max_execution_time],
    ['-t', '--resourcetimeout NUMBER', 'How many ms to wait for each resource to load, defaults to ' + args.resource_timeout],
]

var parser = new optparse.OptionParser(switches);
parser.banner = 'USAGE: phantomjs take_screenshot http://url-to-screenshot.com'

parser.on('help', function() {
    console.log(parser.toString());
    phantom.exit();
});

parser.on(1, function(val){
    var likely_url = new RegExp('^http(s)?://.*');
    if (likely_url.test(val)){
        url = val;    
    } else {
        console.log("FATAL: You didn't provide a valid url");
        phantom.exit(1);        
    }
});

parser.on('*', function(opt, value) {
    if (typeof args[opt] !== 'undefined') {
        console.log('setting ' + opt + ' to ' + value )
        args[opt] = value
    }
});

parser.parse(system.args);

if (typeof url == 'undefined') {
    console.log("FATAL: You didn't provide a url");
    phantom.exit(1);
}

page.viewportSize = { 
    width: args.width,
    height: args.height
};

if (args.crop_to_visible) {
    page.clipRect = {
        top: 0,
        left: 0,
        width: pageWidth,
        height: pageHeight 
    }   
}

// Settings for page open
page.settings.userAgent = args.user_agent
page.settings.resourceTimeout = args.resource_timeout;

// Add in some error handling
page.onResourceError = function(resourceError) {
    page.reason = resourceError.errorString;
    page.reason_url = resourceError.url;
};

try {
    page.open(url, function (status) {
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
                var final_url = page.url
                if(final_url != url){
                    console.log('REDIRECTED_TO: ' + final_url)
                }
                
                for (a in args) {
                    console.log('ARG[' + a + ']' + ' ' + args[a]);
                }

                output_path = args.dir + '/' + args.name + '.' + args.ext;
                page.render(output_path, {format: args.ext, quality: args.quality});
                console.log('SAVED IMAGE: '+ output_path);
                phantom.exit();

            }, args.render_after);
        }
    });

} finally {
    setTimeout(function() {
        console.log('Status: FAILED')
        console.log("Max execution time " + args.max_execution_time + " exceeded");
        phantom.exit(1);
    }, args.max_execution_time);
}
