import { Header } from '../components/Header'
import { Footer } from '../components/Footer'
import Head from 'next/head'
import styles from '../styles/divulgar-vaga-no-ITA.module.scss'

export default function DivulgarVagaITA() {
	return (
		<>
			<Head>
				<title>Divulgar Vaga | CEE</title>
			</Head>
			<Header />
			<div className={styles.container}>
				<h1>Divulgar Vaga no ITA</h1>
			</div>
			<Footer />
		</>
	)
}
