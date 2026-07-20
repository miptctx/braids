import { defineConfig } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3'


// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Braids, knots and links calculation results",
  description: "This website contains calculations of braids, knots and links invariants",
  markdown: {
    config: (md) => {
      md.use(mathjax3)
    }
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      // { text: 'Examples', link: '/markdown-examples' }
    ],

    /*
    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      }
    ],
    */

    socialLinks: [
      { icon: 'github', link: 'https://github.com/miptctx/braids' }
    ]
  }
})
