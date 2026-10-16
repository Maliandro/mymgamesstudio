<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8"/>
<xsl:template match="/">
<html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>RSS · MEYADE GAMES STUDIO</title><meta name="robots" content="noindex"/>
<style>
body{margin:0;background:#0a0e16;color:#e8edf3;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.6}
.w{max-width:720px;margin:0 auto;padding:40px 16px}
h1{margin:0 0 6px;font-size:28px;letter-spacing:.5px}
.note{background:#121a26;border:1px solid #1f2b3b;border-radius:12px;padding:14px 16px;color:#a9b8c8;font-size:15px;margin:18px 0 28px}
code{background:#0d131d;padding:2px 6px;border-radius:6px;color:#28d7be}
a{color:#28d7be}
.it{border-top:1px solid #1a2433;padding:18px 0}
.it a{font-weight:700;font-size:18px;color:#fff;text-decoration:none}
.it a:hover{color:#28d7be}
.d{color:#8fa0b3;font-size:13px}.s{color:#c3cfdb;margin:6px 0 0}
</style></head><body><div class="w">
<h1>MEYADE GAMES STUDIO blog</h1>
<div class="note">This is an RSS feed. Copy this address into a feed reader (Feedly, Inoreader, NetNewsWire…) to get new stories:<br/><code><xsl:value-of select="/rss/channel/atom:link/@href" xmlns:atom="http://www.w3.org/2005/Atom"/></code><br/>Or go back to <a href="/blog/">the blog</a>.</div>
<xsl:for-each select="/rss/channel/item">
<div class="it"><a href="{link}"><xsl:value-of select="title"/></a>
<div class="d"><xsl:value-of select="substring(pubDate,1,16)"/></div>
<p class="s"><xsl:value-of select="description"/></p></div>
</xsl:for-each>
</div></body></html>
</xsl:template></xsl:stylesheet>
