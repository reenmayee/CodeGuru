// components/ai_response_box.jsx
import ReactMarkdown from "react-markdown";

export default function AIResponseBox({ output }) {
  return (
    <div className="border rounded p-4 my-4 bg-gray-100 min-h-[150px] overflow-auto">
      {output ? (
        <ReactMarkdown>{output}</ReactMarkdown>
      ) : (
        "AI response will appear here."
      )}
    </div>
  );
}
