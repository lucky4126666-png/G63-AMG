import { useEffect, useState } from "react"

export default function App() {
  const [stats, setStats] = useState({})

  useEffect(() => {
    fetch("/stats").then(r => r.json()).then(setStats)
  }, [])

  return (
    <div style={{padding:20}}>
      <h1>🚀 Dashboard</h1>
      <p>Users: {stats.users}</p>
      <p>Messages: {stats.messages}</p>
      <p>Jobs: {stats.jobs}</p>
    </div>
  )
}
