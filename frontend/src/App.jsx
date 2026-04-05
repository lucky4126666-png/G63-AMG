import { useEffect, useState } from "react"

export default function App() {
  const [stats, setStats] = useState(null)

  useEffect(() => {
    fetch("/api/stats").then(r => r.json()).then(setStats)
  }, [])

  return (
    <div style={{padding:20, background:"#0f172a", color:"white", minHeight:"100vh"}}>
      <h1>🚀 AI Dashboard</h1>

      {stats ? (
        <>
          <p>👤 Users: {stats.users}</p>
          <p>💬 Messages: {stats.messages}</p>
        </>
      ) : "Loading..."}

      <button style={{
        background:"linear-gradient(45deg,#6366f1,#ec4899)",
        padding:12,
        borderRadius:10,
        border:"none",
        color:"white"
      }}>
        🤖 AI Action
      </button>
    </div>
  )
}
