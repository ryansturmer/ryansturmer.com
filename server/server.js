require('shelljs/global');
var githubhook = require('githubhook');
var github = githubhook({
	'host':'localhost',
	'port':3420,
	'path':'/'
});
github.listen()
github.on('push:ryansturmer.com', function(ref, data) {
	cd('/home/ryansturmer/ryansturmer.com/src/ryansturmer.com/')
	exec('git pull origin master')
	exec('make html-production')
});
