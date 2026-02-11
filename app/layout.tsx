import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Hello World App",
  description: "シンプルなNext.js Hello World アプリケーション",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ja">
      <body>{children}</body>
    </html>
  );
}
