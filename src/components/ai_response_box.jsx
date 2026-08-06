// components/ai_response_box.jsx
export default function AIResponseBox({ output }) {
  return (
    <div className="border rounded p-4 my-4 bg-gray-100 min-h-[150px] whitespace-pre-wrap">
      {output || 'AI response will appear here.'}
    </div>
  );
}
