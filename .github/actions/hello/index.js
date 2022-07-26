// install the package https://github.com/actions/toolkit
// install  https://github.com/vercel/ncc
// - we need this package to setup all the dependencies and libraries in one file, otherwise the GitHub Actions unable to find the package
// eg, ncc build .\.github\actions\hello\index.js -o .\.github\actions\hello\dist\
const core = require('@actions/core');
const github = require('@actions/github');

try{
    // throw( new Error("Some error message"));
    
    // the debug message will only appear if debugging is enabled
    core.debug('Debug message');
    core.warning('Warning message');
    core.error('Error message');

    const name = core.getInput('who-to-greet');
    core.setSecret(name)
    console.log(`Hello ${name}`);

    const time = new Date();
    core.setOutput("time", time.toTimeString());

    // expandable
    core.startGroup('Logging github object');
    console.log(JSON.stringify(github, null, '\t'));
    core.endGroup();

    // export env variable
    core.exportVariable('HELLO', 'hello');
}
catch(error) {
    // if we do not call this function, the GitHub Action will always is success
    core.setFailed(error.message);
}
