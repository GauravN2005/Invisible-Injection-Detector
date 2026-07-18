import { useState } from "react";
import API from "../api";

function Dashboard() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzePrompt = async () => {
    if (!prompt.trim()) return alert("Please type or paste a prompt first!");
    
    setLoading(true);
    try {
      const res = await API.post("/analyze", { prompt: prompt });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Backend not connected! Displaying mock threat telemetry for testing.");
      
      // Mock fallback data mapping exactly to your backend metrics
      setResult({
        risk: 94,
        attack: "Base64 Obfuscation payload",
        status: "Blocked",
      });
    } finally {
      setLoading(false);
    }
  };

  // Inline styling objects to replace Tailwind
  const styles = {
    container: { display: "flex", height: "100vh", backgroundColor: "#0f172a", color: "#f1f5f9", fontFamily: "sans-serif" },
    sidebar: { width: "240px", backgroundColor: "#020617", borderRight: "1px solid #334155", padding: "24px", display: "flex", flexDirection: "column", justifyContent: "between" },
    logoArea: { display: "flex", alignItems: "center", gap: "12px", marginBottom: "32px" },
    logoIcon: { height: "32px", width: "32px", borderRadius: "8px", backgroundColor: "#dc2626", display: "flex", alignItems: "center", justifyValue: "center", fontWeight: "bold", color: "white", paddingLeft: "6px", boxSizing: "border-box" },
    logoText: { fontWeight: "bold", fontSize: "18px", color: "white" },
    navLink: { display: "block", padding: "10px 16px", borderRadius: "8px", backgroundColor: "#1e293b", color: "white", fontWeight: "500", textDecoration: "none" },
    main: { flex: 1, overflowY: "auto", padding: "32px" },
    header: { marginBottom: "32px" },
    title: { fontSize: "28px", fontWeight: "700", color: "white", margin: 0 },
    subtitle: { color: "#94a3b8", marginTop: "4px", fontSize: "14px" },
    grid: { display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: "32px" },
    card: { backgroundColor: "#020617", border: "1px solid #1e293b", borderRadius: "12px", padding: "24px", display: "flex", flexDirection: "column" },
    cardTitle: { fontSize: "16px", fontWeight: "600", color: "#e2e8f0", marginTop: 0, marginBottom: "16px", display: "flex", alignItems: "center", gap: "8px" },
    pulseDot: { h: "8px", w: "8px", borderRadius: "50%", backgroundColor: "#10b981", display: "inline-block" },
    textarea: { width: "100%", height: "200px", backgroundColor: "#0f172a", border: "1px solid #1e293b", borderRadius: "8px", padding: "16px", color: "#f8fafc", placeholderColor: "#64748b", outline: "none", resize: "none", boxSizing: "border-box" },
    button: { marginTop: "16px", width: "100%", backgroundColor: "#dc2626", color: "white", fontWeight: "500", padding: "12px", borderRadius: "8px", border: "none", cursor: "pointer", transition: "all 0.2s" },
    metricsRow: { display: "grid", gridTemplateColumns: "1fr 1fr", gap: "16px", marginBottom: "20px" },
    metricWidget: { backgroundColor: "#0f172a", border: "1px solid #1e293b", padding: "20px", borderRadius: "12px" },
    metricLabel: { fontSize: "12px", fontWeight: "600", textTransform: "uppercase", tracking: "wider", color: "#94a3b8", display: "block", marginBottom: "4px" },
    riskValue: (risk) => ({ fontSize: "36px", fontWeight: "800", color: risk > 70 ? "#ef4444" : risk > 40 ? "#eab308" : "#10b981", margin: 0 }),
    statusBadge: (status) => ({ inlineFlex: "center", padding: "6px 12px", borderRadius: "9999px", fontSize: "14px", fontWeight: "600", border: "1px solid", backgroundColor: status === "Blocked" ? "rgba(239, 68, 68, 0.1)" : "rgba(16, 185, 129, 0.1)", color: status === "Blocked" ? "#f87171" : "#34d399", borderColor: status === "Blocked" ? "rgba(239, 68, 68, 0.3)" : "rgba(16, 185, 129, 0.3)", marginTop: "8px", display: "inline-block" }),
    threatBlock: { backgroundColor: "#0f172a", border: "1px solid #1e293b", padding: "20px", borderRadius: "12px" },
    threatBox: { display: "flex", alignItems: "center", gap: "12px", backgroundColor: "#020617", padding: "12px", borderRadius: "8px", border: "1px solid #1e293b", marginTop: "8px" },
    threatText: { margin: 0, fontFamily: "monospace", fontSize: "14px", fontWeight: "700", color: "#e2e8f0" },
    idleState: { flex: 1, border: "2px dashed #1e293b", borderRadius: "12px", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", padding: "32px", textAlign: "center", backgroundColor: "rgba(15, 23, 42, 0.2)" }
  };

  return (
    <div style={styles.container}>
      
      {/* Sidebar Layout */}
      <aside style={styles.sidebar}>
        <div>
          <div style={styles.logoArea}>
            <div style={styles.logoIcon}>🛡️</div>
            <span style={styles.logoText}>PromptShield</span>
          </div>
          <nav>
            <a href="#" style={styles.navLink}>Threat Gateway</a>
          </nav>
        </div>
        <div style={{ fontSize: "12px", color: "#475569", borderTop: "1px solid #1e293b", paddingTop: "16px" }}>
          Core Engine • v1.0
        </div>
      </aside>

      {/* Main Panel Content */}
      <main style={styles.main}>
        <header style={styles.header}>
          <h1 style={styles.title}>AI Firewall Telemetry</h1>
          <p style={styles.subtitle}>Real-time isolation sandbox for untrusted prompt injection payloads.</p>
        </header>

        <div style={styles.grid}>
          
          {/* Input Configuration Column */}
          <div style={styles.card}>
            <h2 style={styles.cardTitle}>
              <span style={styles.pulseDot}></span>
              Payload Interrogation
            </h2>
            <textarea
              style={styles.textarea}
              placeholder="Paste raw user prompt query or string vectors to evaluate security risks..."
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
            />
            <button
              onClick={analyzePrompt}
              disabled={loading}
              style={styles.button}
            >
              {loading ? "Analyzing Stream..." : "Evaluate Telemetry"}
            </button>
          </div>

          {/* Metrics Inspection Column */}
          <div style={styles.card}>
            <h2 style={styles.cardTitle}>Inspection Response Metrics</h2>
            
            {result ? (
              <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>
                
                {/* Metric Widgets Row */}
                <div style={styles.metricsRow}>
                  
                  {/* Metric 1: Risk Score UI */}
                  <div style={styles.metricWidget}>
                    <span style={styles.metricLabel}>Risk Score</span>
                    <p style={styles.riskValue(result.risk)}>{result.risk}%</p>
                  </div>

                  {/* Metric 2: Mitigation Status UI */}
                  <div style={styles.metricWidget}>
                    <span style={styles.metricLabel}>Mitigation Status</span>
                    <span style={styles.statusBadge(result.status)}>{result.status}</span>
                  </div>
                </div>

                {/* Metric 3: Threat Classification Block */}
                <div style={styles.threatBlock}>
                  <span style={styles.metricLabel}>Identified Attack Classification</span>
                  <div style={styles.threatBox}>
                    <span style={{ fontSize: "18px" }}>🧬</span>
                    <p style={styles.threatText}>{result.attack || "No Threat Signatures Found"}</p>
                  </div>
                </div>

              </div>
            ) : (
              <div style={styles.idleState}>
                <span style={{ fontSize: "40px", marginBottom: "12px", opacity: 0.4 }}>⚙️</span>
                <p style={{ color: "#94a3b8", fontWeight: "500", fontSize: "14px", margin: "0 0 4px 0" }}>Awaiting Network Stream Data</p>
                <p style={{ fontSize: "12px", color: "#475569", margin: 0, maxWidth: "260px" }}>
                  Run evaluation scans to stream live JSON metrics into the monitoring dashboard.
                </p>
              </div>
            )}
          </div>

        </div>
      </main>
    </div>
  );
}

export default Dashboard;