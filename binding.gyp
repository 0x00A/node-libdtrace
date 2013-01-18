{
  'targets': [
    {
      'target_name': 'dtrace',
      'include_dirs': [
      ],
      'sources': [
        'libdtrace.cc',
      ],
      'libraries': ['-ldtrace'],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '-fcxx-exceptions'
        ]
      }
    }
  ]
}