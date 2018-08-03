(function(plugins){
  var do_feature_product = function(config){
    var spam_timer = false;
    var spam_buffer = false;
    var active_feed = '';
    var featured_nav = '';
    var key_links = {};
    var feed_keys = {};
    var c = 0;

    mF.$(function(){
      //cordinate the tabs if needed.

      var selector = '', nav = '', feed = '', item = '', selector_values = '';

      for (var C in config.feed_selectors){c++;}
      if (c > 1){
        var nav_key = '';
        for (selector in config.feed_selectors) {
          selector_values = config.feed_selectors[selector];
          if(mF.$.isArray(selector_values)) {
            key_links[selector] = [];
            mF.$.each(selector_values, function(idx, value) {
              key_links[selector].push(mF.$(value).parent().attr('data-nav_key'));
            });
          } else {
            key_links[selector] = [mF.$(selector_values).parent().attr('data-nav_key')];
          }

          var feature_key = key_links[selector];
          var ad_content_keys = mF.ad.content_keys;
          for (nav in ad_content_keys){
            for (feed in ad_content_keys[nav].content_keys){
              var feed_config = ad_content_keys[nav].content_keys[feed].config;
              if (feed_config.key == key_links[selector]){
                feed_keys[selector] = feed_config.feed_key;
              }

              if (feed_config.key == feature_key){
                featured_nav = nav;
                feed_keys[selector] = feed_config.feed_key;
                nav_key = mF.ad.content_keys[nav];
                active_feed = nav_key.content_keys[nav_key.config.default_key].config.feed_key;
              }
            }
          }
          mF.$(selector+'_nav_item a').on('click',nav_sync(nav_key, feature_key));
        }
      }else{
        //do just one.
        for (selector in config.feed_selectors){

          selector_values = config.feed_selectors[selector];

          if(!mF.$.isArray(selector_values))
            selector_values = [selector_values];

          for (item in mF.ad.content_keys){

            mF.$.each(selector_values, function(idx, value) {
              if (mF.ad.content_keys[item].config.selector == value){
                feed_keys[selector] = active_feed = mF.ad.content_keys[item].config.feed_key;
                if (!key_links[selector])
                  key_links[selector] = [];

                key_links[selector].push(mF.ad.content_keys[item].config.key);
              }
            });

          }
        }
      }
      update_preview();
    });

    var update_preview = function(){
      if (spam_buffer){return;}
      spam_buffer = true;
      spam_timer = setTimeout(function(){spam_buffer = false; clearTimeout(spam_timer);},500);
      for (var item in config.feed_selectors){
        if (feed_keys[item] == active_feed){
          var active_slider = mF.$(item+' .items_viewport.active');
          if (active_slider.length > 0) {
            var num_char = mF.integerID(active_slider.prop('id'));
            var replace_num = (num_char + config.offset_from_active + mF.feeds.datas[active_feed].length)%(mF.feeds.datas[active_feed].length);
            active_slider = active_slider.prop('id').replace(''+num_char,''+replace_num);

            var selector_values = config.feed_selectors[item];

            if(!mF.$.isArray(selector_values))
              selector_values = [selector_values];

            mF.$.each(selector_values, function(idx, value) {
              var details_to_activate = ('#'+active_slider).replace(item, value).substring(1);
              if (!mF.$('#'+details_to_activate).hasClass('active')) {
                if (c > 1){
                  mF.$.each(key_links[item], function(idx, feed_key) {
                    mF.ad.content_keys[featured_nav].content_keys[feed_key].transition.changeTo(details_to_activate);
                  });
                }else{
                  mF.$.each(key_links[item], function(idx, feed_key) {
                    mF.ad.content_keys[feed_key].transition.changeTo(details_to_activate);
                  });
                }
              }
            });
          }
        }
      }
    }

    var nav_sync = function(nav_key, feed_key){
      return function(){
        active_feed = nav_key.content_keys[feed_key].config.feed_key;
        nav_key.changeActiveFromKey(feed_key);
      };
    }

    //register the code into the config object.
    if (typeof mF.config.api == 'undefined'){mF.config.api = {};}
    if (typeof mF.config.api.register == 'undefined'){mF.config.api.register = {};}
    if (typeof mF.config.api.register['_transition_set_active'] == 'undefined'){
      mF.config.api.register['_transition_set_active'] = [update_preview];
    }else{
      mF.config.api.register['_transition_set_active'].push(update_preview);
    }

  }
  for (var plugin in plugins){
    if (plugins[plugin].type == 'feature_product'){
      do_feature_product(plugins[plugin]);
    }
  }
})(mF.plugins)