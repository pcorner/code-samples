{
  'targets': [
    {
      'target_name': 'addonP',
      'sources': [ 'AddonP.cc', 'DataProcessingAsyncWorker.cc' ],
      'include_dirs': ["<!@(node -p \"require('node-addon-api').include\")", "./"],
      'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
    }
  ]
}
