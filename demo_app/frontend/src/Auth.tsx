import { useState } from 'react';
import './Auth.css';


type AuthFormProps = {
  onAuth: (token: any) => void;
};

export default function AuthForm({ onAuth }: AuthFormProps) {
  const [clientId, setClientId] = useState<string>('');
  const [clientSecret, setClientSecret] = useState<string>('');
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [scope, setScope] = useState<string>('securitiesservices');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const res = await fetch('/auth/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          client_id: clientId,
          client_secret: clientSecret,
          username,
          password,
          scope,
        }),
      });
      if (!res.ok) throw new Error('Falha na autenticação');
      const data = await res.json();
      onAuth(data);
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('Erro desconhecido');
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <form className="auth-form" onSubmit={handleSubmit}>
      <h2>Autenticação XP</h2>
      <label>
        Client ID
        <input value={clientId} onChange={e => setClientId(e.target.value)} required />
      </label>
      <label>
        Client Secret
        <input value={clientSecret} onChange={e => setClientSecret(e.target.value)} required type="password" />
      </label>
      <label>
        Username
        <input value={username} onChange={e => setUsername(e.target.value)} required />
      </label>
      <label>
        Password
        <input value={password} onChange={e => setPassword(e.target.value)} required type="password" />
      </label>
      <label>
        Scope
        <input value={scope} onChange={e => setScope(e.target.value)} />
      </label>
      <button type="submit" disabled={loading}>
        {loading ? 'Autenticando...' : 'Autenticar'}
      </button>
      {error && <div className="auth-error">{error}</div>}
    </form>
  );
}
