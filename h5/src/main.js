import { createApp } from 'vue'
import App from './App.vue'
import { 
  Calendar,
  Cell, 
  CellGroup,
  Loading,
  Toast 
} from 'vant'
import 'vant/lib/index.css'

const app = createApp(App)

app.use(Calendar)
   .use(Cell)
   .use(CellGroup)
   .use(Loading)
   .use(Toast)

app.mount('#app') 