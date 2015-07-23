// Generated by CoffeeScript 1.9.2
require.config({
  urlArgs: "bust=" + (new Date()).getTime(),
  waitSeconds: 200,
  paths: {
      "jquery": "vendor/jquery/dist/jquery",
      "cookie": "vendor/jquery/dist/jquery.cookie",
      "react": "vendor/react/react",
      "dispatcher": "vendor/flux/dist/lib/Dispatcher",
      "invariant": "vendor/flux/dist/lib/invariant",
    //   "flux": "vendor/flux/dist/Flux",
      "microevent": "vendor/events/microevent",
      "addons": "vendor/react/react-with-addons",
      "bootstrap": "vendor/bootstrap/dist/js/bootstrap",
      "snackbars": "vendor/snackbarjs/dist/snackbar.min",

      "Auth": "develop/auth/AuthView",
      "Registration": "develop/auth/RegistrationView",
      "Navigation": "develop/navigation/NavigationView",
      "AppView": "develop/posts/app",
      "AddPost": "develop/posts/AddPostView",
      "AppActions": "develop/auth/AppActions",
      "AppStore": "develop/auth/AppStore",
      "AppDispatcher": "develop/auth/AppDispatcher"
  },
  shim: {
      "cookie": {
          "deps": ['jquery']
      },
      "bootstrap": {
          "deps": ['jquery']
      },
      "snackbars": {
          "deps": ['jquery']
      },
      "dispatcher": {
          "deps": ['invariant']
      },
      "Navigation": {
          "deps": ['Auth']
      },
      "AppActions": {
          "deps": ['dispatcher', 'microevent']
      },
    //   "material": {
    //       "material": "vendor/bootstrap-material-design/dist/js/material",
    //       "ripples": "vendor/bootstrap-material-design/dist/js/ripples"
    //   },
  }
});

require(['AppView', 'Navigation', 'AddPost'], function(AppView) {
  var appView;
  appView = new AppView;
});
