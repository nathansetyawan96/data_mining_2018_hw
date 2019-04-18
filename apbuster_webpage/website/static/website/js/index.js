var main = document.getElementsByClassName('aqposts')[0]
var posts = main.getElementsByClassName('aqpost')

for (var i = 0; i < posts.length; i++) {
  var aqi = posts[i].getElementsByClassName('post-aqi')[0].innerHTML
  var addingColor = (index) => {
    var color = ''
    if (index <= 11) color = '#9CFF9C'
    else if (index <= 23) color = '#31FF00'
    else if (index <= 35) color = '#30CE00'
    else if (index <= 41) color = '#FEFF00'
    else if (index <= 47) color = '#FFCF03'
    else if (index <= 53) color = '#FF9A01'
    else if (index <= 58) color = '#FF6465'
    else if (index <= 64) color = '#FF0000'
    else if (index <= 70) color = '#990000'
    else if (index >= 71) color = '#CE30FF'
    return color
  }
  var color = addingColor(aqi)
  posts[i].style.backgroundColor = color
}

// 0-11 #9CFF9C
// 12-23 #31FF00
// 24-35 #30CE00
// 36-41 #FEFF00
// 42-47 #FFCF03
// 48-53 #FF9A01
// 54-58 #FF6465
// 59-64 #FF0000
// 65-70 #990000
// >71 #CE30FF
