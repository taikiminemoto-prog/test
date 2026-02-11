export default function Home() {
  return (
    <main
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        minHeight: "100vh",
        padding: "20px",
        backgroundColor: "#f5f5f5",
      }}
    >
      <h1
        style={{
          fontSize: "48px",
          fontWeight: "bold",
          color: "#333",
          margin: "0 0 20px 0",
        }}
      >
        Hello World
      </h1>
      <p
        style={{
          fontSize: "18px",
          color: "#666",
          maxWidth: "500px",
          textAlign: "center",
          lineHeight: "1.6",
        }}
      >
        へようこそ！これはNext.js（App Router）で作られたシンプルなWebアプリケーションです。
        React と Next.js を使用した最小限の構成で実装されています。
      </p>
    </main>
  );
}
