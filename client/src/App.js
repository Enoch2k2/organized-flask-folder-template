import { useEffect } from 'react';
import './App.css';

function App() {
  useEffect(() => {
    fetch("/api/books")
      .then(resp => resp.json())
      .then(data => console.log(data))
  }, [])  

  return (
    <div className="App">
      <h1>Hello World</h1>
    </div>
  );
}

export default App;
