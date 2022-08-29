let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let  myWatchedSeriesLength=["peaky blender","blacklist","prison break"];
let myWatchedSeriesSentence=["Un groupe de gangster","serie enquete","liberation de son frere de prison"];

console.log("I watch 3 series: "+myWatchedSeriesLength);
myWatchedSeries[2]="friends";
myWatchedSeries.push("black said");
myWatchedSeries.unshift("sillicon valley");
myWatchedSeries.splice(1,1);
console.log(myWatchedSeries)