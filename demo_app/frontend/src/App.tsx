import { useState } from 'react';
import './App.css';
import AuthForm from './Auth';

function App() {
  const [token, setToken] = useState(null);

  if (!token) {
    return <AuthForm onAuth={setToken} />;
  }

  return (
    <div style={{ color: '#eee', background: '#222', minHeight: '100vh', padding: '2rem' }}>
      <h2>Autenticado!</h2>
      <pre style={{ background: '#333', color: '#fff', padding: '1rem', borderRadius: '8px' }}>
        {JSON.stringify(token, null, 2)}
      </pre>
      {/* Aqui você pode renderizar as interfaces dos outros endpoints */}
    </div>
  );
}

export default App
