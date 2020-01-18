/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) 
{
  return address.replace(/\./g, '[.]');
};


//var x = defangIPaddr("12.3.4.5.6");
//console.log(x)
//another oneliner
