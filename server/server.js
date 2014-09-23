var githubhook = require('githubhook');
var github = githubhook({
	'host':'localhost',
	'port':3420,
	'path':'/github/callback'
});

github.listen();

github.on('*', function(event, repo, ref, data) {
	console.log(event);
	console.log(repo);
	console.log(ref);
	console.log(data);
});