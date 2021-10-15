window.npup = (function (containerId, baseId) {
  // save the container of your special element
  var elementsContainer = document.getElementById(containerId);
  function doSelect(select) {
    // get value of select
    var value = select.value;
    // find element based on the value of the select
    var selected = findElement(value);
    if (!selected) {
      return;
    } // didn't find the element, bail
    // do hiding/showing of elements
    hideAll(elementsContainer);
    showElement(selected);
  }
  // retrieve some element based on the value submitted
  function findElement(value) {
    return document.getElementById(baseId + value);
  }
  // hide all element nodes within some parent element
  function hideAll(parent) {
    var children = parent.childNodes,
      child;
    // loop all the parent's children
    for (var idx = 0, len = children.length; idx < len; ++idx) {
      child = children.item(idx);
      // if element node (not comment- or textnode)
      if (child.nodeType === 1) {
        // hide it
        child.style.display = "none";
      }
    }
  }
  // display a certain element
  function showElement(element) {
    element.style.display = "";
  }
  // hide all on page load (might want some extra logic here)
  hideAll(elementsContainer);

  // export api to use from select element's onchange or so
  return {
    doSelect: doSelect
  };
})("mySpecialElements", "npup"); // give the routine a container id of your special elements, and the base id of those elements
