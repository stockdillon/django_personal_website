var Swiftype = window.Swiftype || {};
Swiftype.root_url = Swiftype.root_url || "//search-api.swiftype.com";
Swiftype.embedVersion = Swiftype.embedVersion || 'v1';
if (typeof Swiftype.renderStyle === 'undefined') {
  Swiftype.renderStyle = 'nocode';
}

Swiftype.isMobile = function() {
  var ua = window.navigator.userAgent;
  if(/iPhone|iPod/.test(ua) && ua.indexOf("AppleWebKit") > -1 ) {
    return true;
  }
  if (/Android/.test(ua) && /Mobile/i.test(ua) && ua.indexOf("AppleWebKit") > -1 ) {
    return true;
  }
  return false;
};

Swiftype.loadScript = function(url, callback) {
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.async = true;
  script.src = url;

  var entry = document.getElementsByTagName('script')[0];
  entry.parentNode.insertBefore(script, entry);

  if (script.addEventListener) {
    script.addEventListener('load', callback, false);
  } else {
    script.attachEvent('onreadystatechange', function() {
      if (/complete|loaded/.test(script.readyState))
        callback();
    });
  }
};

Swiftype.loadStylesheet = function(url) {
  var link = document.createElement('link');
  link.rel = 'stylesheet';
  link.type = 'text/css';
  link.href = url;
  (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(link);
};

Swiftype.loadSupportingFiles = function(callback) {
  if (Swiftype.renderStyle === false) {
    Swiftype.loadScript("//s.swiftypecdn.com/assets/swiftype_no_render-8bb748e54daefb0868a4f00b7e747fb7.js", callback);
    Swiftype.loadStylesheet("//s.swiftypecdn.com/assets/swiftype-e91a60519fa93c33f89c5611838bd149.css");
  } else if (Swiftype.isMobile() && !Swiftype.disableMobileOverlay) {
    Swiftype.loadScript("//s.swiftypecdn.com/assets/swiftype_nocode-887a1d7023fd5e7912102c902d625f68.js", callback);
    Swiftype.loadStylesheet("//s.swiftypecdn.com/assets/swiftype_nocode-841601ba635e8ac17871e4c70b068be7.css");
  } else if (Swiftype.renderStyle === 'inline' || Swiftype.renderStyle === 'new_page') {
    Swiftype.loadScript("//s.swiftypecdn.com/assets/swiftype_onpage-470cab1e39526c8a397e5539a686ed38.js", callback);
    Swiftype.loadStylesheet("//s.swiftypecdn.com/assets/swiftype-e91a60519fa93c33f89c5611838bd149.css");
  } else {
    Swiftype.loadScript("//s.swiftypecdn.com/assets/swiftype_nocode-887a1d7023fd5e7912102c902d625f68.js", callback);
    Swiftype.loadStylesheet("//s.swiftypecdn.com/assets/swiftype_nocode-841601ba635e8ac17871e4c70b068be7.css");
  }
};

var Swiftype = (function(window, undefined) {
   if (Swiftype.embedVersion === 'v1') {
     Swiftype.loadSupportingFiles(function(){});
   }
   return Swiftype;
})(window);
