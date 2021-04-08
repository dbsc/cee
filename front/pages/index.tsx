import Head from 'next/head'
import { Hero } from '../components/Hero'
import { Numeros } from '../components/Numeros'
import { Servicos } from '../components/Servicos'
import { Parceiros } from '../components/Parceiros'

import styles from '../styles/index.module.scss'
export default function Home() {
	return (
		<>
			<Head>
				<title>Início | CEE</title>
			</Head>

			<Hero />

			<Numeros />

			<Servicos />

			<Parceiros />

			{/* <div className={styles.container}>
				<img src="/images/aguia.svg" alt="Águia" />
			</div> */}
		</>
	)
}
