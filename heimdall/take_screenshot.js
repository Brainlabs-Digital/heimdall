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
args.useragent = 'heimdall';
args.croptovisible = false;
args.maxexecutiontime = 30000;
args.renderafter = 7000;
args.resourcetimeout = 3000;

var switches = [
    ['--help', 'Show the help'],
    ['-h', '--height NUMBER', 'Set the height, defaults to ' + args.height],
    ['-w', '--width NUMBER', 'Set the height, defaults to ' + args.width],
    ['-u', '--useragent TEXT', 'The useragent to set, defaults to ' + args.useragent],
    ['-c', '--croptovisible TEXT', 'Include the whole webpage or just the visible bit, defaults to ' + args.croptovisible],    
    ['-d', '--dir TEXT', 'The folder to save to, defaults to ' + args.dir],
    ['-n', '--name TEXT', 'The name of the image to save, defaults to ' + args.name],
    ['-e', '--ext TEXT', 'The extension (and hence format) of the saved image, defaults to ' + args.ext],
    ['-q', '--quality NUMBER', 'The quality of the image to save, defaults to ' + args.quality],
    ['-r', '--renderafter NUMBER', 'How many ms to wait before we render, defaults to ' + args.renderafter],
    ['-m', '--maxexecutiontime NUMBER', 'How many ms to wait before we die, defaults to ' + args.maxexecutiontime],
    ['-t', '--resourcetimeout NUMBER', 'How many ms to wait for each resource to load, defaults to ' + args.resourcetimeout],
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

if (args.croptovisible) {
    page.clipRect = {
        top: 0,
        left: 0,
        width: pageWidth,
        height: pageHeight 
    }   
}

// Settings for page open
page.settings.userAgent = args.useragent
page.settings.resourceTimeout = args.resourcetimeout;

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

            }, args.renderafter);
        }
    });

} finally {
    setTimeout(function() {
        console.log('Status: FAILED')
        console.log("Max execution time " + args.maxexecutiontime + " exceeded");
        phantom.exit(1);
    }, args.maxexecutiontime);
}
