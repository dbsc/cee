import Head from 'next/head'
import styles from '../styles/contato.module.scss'
import { Header } from '../components/Header'
import { Footer } from '../components/Footer'
import { ContatoTitle } from '../components/ContatoTitle'
import { FormsRedes } from '../components/FormsRedes'

export default function Contato() {
	return (
		<>
			<Head>
				<title>Contato | CEE</title>
			</Head>
			<Header />

			<ContatoTitle />
			<FormsRedes />
			<Footer />
		</>
	)
}
