// Inputs
// inputs: An array of inputs.
// limit: The maximum number of operations at any one time.
// iterateeFn: The async function that should be called with each input to generate the corresponding output. It will have two arguments:
//      input: The input being processed.
//      callback: A function that will be called when the input is finished processing. It will be provided one argument, the processed output.
// callback: A function that should be called with the array of outputs once all the inputs have been processed.

function getNameById(id, callback) {
  // simulating async request
  const randomRequestTime = Math.floor(Math.random() * 100) + 200;
 
  setTimeout(() => {
    callback("User" + id)
  }, randomRequestTime);
}

function groupBy(inputs, limit) {
  let nOfGroups = Math.ceil(inputs.length/limit);
  const groups = {};

  for(i=0; i<nOfGroups; i++) {
    groups[i] = [];
  }

  for(i=0; i<inputs.length; i++) {
    let groupIndex = Math.floor(i / limit);
    groups[groupIndex].push(inputs[i]);
  }

  return {groups, nOfGroups};
}

function getIterateePromise(iterateeFn, id) {
  return new Promise((resolve) => iterateeFn(id, resolve));
}

async function mapLimit(inputs, limit, iterateeFn, callback) {
  const {groups, nOfGroups} = groupBy(inputs, limit);

  console.log(groups);
    const output = [];
    for(i=0; i<nOfGroups; i++) {
      const promises = [];
      for(j=0; j<groups[i].length; j++) {
        promises.push(getIterateePromise(iterateeFn, groups[i][j]));
      }
      output.push(...(await Promise.all(promises))); 
    }
    
  callback(output);
}

mapLimit([1,2,3,4,5], 2, getNameById, (allResults) => {
  console.log('output:', allResults) // ["User1", "User2", "User3", "User4", "User5"]
})
