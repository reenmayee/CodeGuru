// components/action_button.jsx
export default function ActionButtons({ onAction }) {
  return (
    <div className="flex justify-center gap-4 my-4">
      <button
        onClick={() => onAction('explain')}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Explain
      </button>
      <button
        onClick={() => onAction('debug')}
        className="bg-yellow-600 text-white px-4 py-2 rounded hover:bg-yellow-700"
      >
        Debug
      </button>
      <button
        onClick={() => onAction('optimize')}
        className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
      >
        Optimize
      </button>
    </div>
  );
}
