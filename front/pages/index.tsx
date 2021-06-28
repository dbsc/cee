import Head from 'next/head'
import { Hero } from '../components/Hero'
import { Numeros } from '../components/Numeros'
import { Servicos } from '../components/Servicos'
import { Feira } from '../components/Feira'
import { Estagios } from '../components/Estagios'
import { Parceiros } from '../components/Parceiros'
import { Header } from '../components/Header'
import { Footer } from '../components/Footer'

import styles from '../styles/index.module.scss'
export default function Home() {
	return (
		<>
			<Head>
				<title>Início | CEE</title>
			</Head>

			<Header />

			<Hero />

			<Numeros />

			<Servicos />

			<Feira />

			<Estagios />

			<Parceiros />

			<Footer />

			{/* <div className={styles.container}>
				<img src="/images/aguia.svg" alt="Águia" />
			</div> */}
		</>
	)
}
