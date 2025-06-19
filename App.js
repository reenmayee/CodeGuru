import { useState } from 'react';
import Header from './components/header.jsx';
import LanguageSelector from './components/lang_selector.jsx';
import CodeEditor from './components/code_editor.jsx';
import ActionButtons from './components/action_button.jsx';
import AIResponseBox from './components/ai_response_box.jsx';

function App() {
  const [language, setLanguage] = useState('javascript');
  const [code, setCode] = useState('// Write your code here');
  const [output, setOutput] = useState("");

  const handleAction = async (type) => {
  try {
    setOutput("Loading...");

    const response = await fetch("http://localhost:5000/review", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        code: code,
        language: language,
        action: type,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      setOutput(`Error: ${errorData.error || 'Unknown error'}`);
      return;
    }

    const data = await response.json();
    setOutput(data.result || "No response from server");
  } catch (error) {
    setOutput(`Network error: ${error.message}`);
  }
};


  return (
    <div className="max-w-3xl mx-auto p-4">
      <Header />
      <LanguageSelector language={language} setLanguage={setLanguage} />
      <p className="text-center mt-2 text-gray-600">Selected Language: {language}</p>
      <CodeEditor code={code} setCode={setCode} language={language} />
      <ActionButtons onAction={handleAction} />
      <AIResponseBox output={output} />
    </div>
  );
}

export default App;
