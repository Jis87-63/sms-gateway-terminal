import React, { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000';

async function get(path) {
  try {
    return await (await fetch(API + path)).json();
  } catch {
    return {};
  }
}

function Card({ title, value }) {
  return <div className="card"><span>{title}</span><b>{value}</b></div>;
}

function App() {
  const [page, setPage] = useState('dashboard');
  const [stats, setStats] = useState({});
  const [gateways, setGateways] = useState([]);
  const [messages, setMessages] = useState([]);
  const [campaigns, setCampaigns] = useState([]);
  const [logs, setLogs] = useState([]);
  const [form, setForm] = useState({ name: '', message: '', numbers: '' });

  async function load() {
    setStats(await get('/stats'));
    setGateways((await get('/gateway/list')).gateways || []);
    setMessages((await get('/message/list')).messages || []);
    setCampaigns((await get('/campaign/list')).campaigns || []);
    setLogs((await get('/logs')).logs || []);
  }

  useEffect(() => {
    load();
    const interval = setInterval(load, 7000);
    return () => clearInterval(interval);
  }, []);

  async function createCampaign() {
    await fetch(API + '/campaign/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: form.name,
        message: form.message,
        numbers: form.numbers.split(/\n|,|;/).map((item) => item.trim()).filter(Boolean),
      }),
    });
    setForm({ name: '', message: '', numbers: '' });
    load();
  }

  return <div className="app"><aside><h1>SMS Gateway</h1>{['dashboard', 'gateways', 'campanhas', 'mensagens', 'logs'].map((item) => <button key={item} onClick={() => setPage(item)} className={page === item ? 'on' : ''}>{item}</button>)}</aside><main>{page === 'dashboard' && <><h2>Dashboard Administrativo</h2><div className="grid"><Card title="Total SMS enviados" value={stats.sent || 0}/><Card title="Pendentes" value={stats.pending || 0}/><Card title="Falhadas" value={stats.failed || 0}/><Card title="Gateways online" value={stats.online_gateways || 0}/><Card title="Campanhas ativas" value={stats.active_campaigns || 0}/></div></>}{page === 'gateways' && <><h2>Gateways</h2><div className="grid">{gateways.map((gateway) => <div className="card" key={gateway.gateway_id}><b>🟢 {gateway.name}</b><p>{gateway.status}</p><p>{gateway.model}</p><p>Bateria {gateway.battery}%</p><p>Enviados: {gateway.sent_count || 0}</p><small>{gateway.gateway_id}</small></div>)}</div></>}{page === 'campanhas' && <><h2>Campanhas</h2><div className="card form"><input placeholder="Nome" value={form.name} onChange={(event) => setForm({ ...form, name: event.target.value })}/><textarea placeholder="Mensagem" value={form.message} onChange={(event) => setForm({ ...form, message: event.target.value })}/><textarea placeholder="Importar números CSV/TXT" value={form.numbers} onChange={(event) => setForm({ ...form, numbers: event.target.value })}/><button onClick={createCampaign}>INICIAR ENVIO</button></div>{campaigns.map((campaign) => <div className="row" key={campaign.id}><b>{campaign.name}</b><span>{campaign.status}</span><span>{campaign.numbers?.length || 0} números</span></div>)}</>}{page === 'mensagens' && <><h2>Mensagens</h2><table><tbody>{messages.map((message) => <tr key={message.id}><td>{message.number}</td><td>{message.message}</td><td>{message.status}</td><td>{message.gateway_id || '-'}</td><td>{message.created_at}</td></tr>)}</tbody></table></>}{page === 'logs' && <><h2>Logs</h2>{logs.map((log, index) => <div className="row" key={index}><b>{log.event}</b><span>{log.created_at}</span></div>)}</>}</main></div>;
}

createRoot(document.getElementById('root')).render(<App />);
