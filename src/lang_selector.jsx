
export default function LanguageSelector({ language, setLanguage }) {
  return (
    <div className="my-2">
      <label htmlFor="language" className="block font-semibold mb-1">Select Language:</label>
      <select
        id="language"
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
        className="border p-2 rounded w-full"
      >
        <option value="javascript">JavaScript</option>
        <option value="python">Python</option>
        <option value="cpp">C++</option>
        <option value="java">Java</option>
        <option value="php">PHP</option>
        <option value="c">C</option>
        {/* Add more languages if needed */}
      </select>
    </div>
  );
}
