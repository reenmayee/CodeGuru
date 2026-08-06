import React from 'react';
import CodeMirror from '@uiw/react-codemirror';

import { javascript } from '@codemirror/lang-javascript';
import { python } from '@codemirror/lang-python';
import { java } from '@codemirror/lang-java';
import { cpp } from '@codemirror/lang-cpp';
import { php } from '@codemirror/lang-php';

import { monokai } from '@uiw/codemirror-theme-monokai';

const langExtensions = {
  javascript: javascript(),
  python: python(),
  java: java(),
  cpp: cpp(),
  c: cpp(),
  php: php(),
};

export default function CodeEditor({ code, setCode, language }) {
  return (
    <div className="my-4">
      <CodeMirror
        value={code}
        height="300px"
        extensions={[langExtensions[language] || javascript()]}
        onChange={setCode}
        theme={monokai}
      />
    </div>
  );
}
