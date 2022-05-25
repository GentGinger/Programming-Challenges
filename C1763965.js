const fs = require('fs');

module.exports = {

    // Exercise 1
    freefall: (val, isD) => {
        //define gravity value
        const g = 9.81;
        // if isD===true then equation finds time, if false then finding Distance
        if (isD===true){
            res = (2*val/g)**0.5;
            return(res.toPrecision(2));
        } else {
            res = 0.5*g*(val**2);
            return(res.toPrecision(2)); 
        }   
    },

    // Exercise 2
    RPS: (s) => {
        //define result
        var res = "";
        //incase of lowercase input convert to uppercase
        res = res.toUpperCase();
        //iterate through s concatenating winning result to res
        for (let c of s) {
            if (c === "R") {
                res += "P";
            } else if(c === "P") {
                res += "S";
            } else {
                res += "R";
            }
        }
        return(res);
    },

    // Exercise 3
    list2str: (l) => {
        function l2s(tos){
            //create variable starting with [
            var res = "[";
            //iterate through l. If element is array run code again, otherwise add element to res
            for (let element of tos) {
                if (Array.isArray(element) === true) {
                    res += l2s(element);
                } else {
                    element = String(element);
                    res += element;
                }
            }
            //end string with ]
            res += "]";
            return(res);
        }
        return(l2s(l))
    },

    // Exercise 4
    textPreprocessing: (text) => {
        //remove punctuation
        var text = text.replace(/[.?!,:;[-\][\]{}()]/g,"");
        //convert all to lower case
        text = text.toLowerCase();
        //convert text to array, splitting at spaces
        text = text.split(" ");
        stopwords = ['i','a','about','am','an','are','as','at','be','by','for','from','how','in','is','it','of','on','or','that','the','this','to','was','what','when','where','who','will','with'];
        //check array text for any stopwords and remove them
        for(let word of text){
            if(stopwords.includes(word)){
                text = text.filter(v => v !== word);
            }
        }
        //remove specified suffixes on words
        for( let word of text){
            if(word.endsWith("ing") === true){
                let wordSuf = word.slice(0, word.length-3);
                text.splice(text.indexOf(word),1 ,wordSuf);
            } else if(word.endsWith("ed") === true){
                let wordSuf = word.slice(0, word.length-2);
                text.splice(text.indexOf(word),1 ,wordSuf);
            } else if(word.endsWith("s") === true){
                let wordSuf = word.slice(0, word.length-1);
                text.splice(text.indexOf(word),1 ,wordSuf);
            }else{
                continue;
            }
        }
        return(text);
    },

    // Exercise 5
    isGreaterThan: (dict1, dict2) => {
    //check if any itmes are in dict2 but not in dict 1. if true ten = false
    for(let key in dict2){
        if(!(key in dict1)){
            var GreaterThan = false;
        } else {
            // find items with the same letter then compare values. If any value in dict2 is higher than dict1 return false, otherwise true
            for(key in dict1){
                if(key in dict2){
                    if(dict1[key] >= dict2[key]){
                        GreaterThan = true;
                    } else {
                        GreaterThan = false;
                        break
                    }
                } else {
                    GreaterThan = true;
                }
            }
        }
    }
    //if to strings are equal return false
    if(JSON.stringify(dict1) === JSON.stringify(dict2)){
        GreaterThan = false;
    }
    return(GreaterThan) 
    },

    // Exercise 6
    CSVsum: (filename) => {
        return undefined;
    },

    // Exercise 7
    str2list: (s) => {
        return undefined;
    },
    
    // Exercise 8
    spacemonSim: (roster1, roster2) => {
        return undefined;
    },

    // Exercise 9
    rewardShortPath: (env) => {
        return undefined;
    },

    // Exercise 10
    cliqueCounter: (network) => {
        return undefined;
    }
}
