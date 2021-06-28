import Head from 'next/head'
import styles from '../styles/quem-somos.module.scss'
import { Header } from '../components/Header'
import { Footer } from '../components/Footer'
import {QSTitle} from '../components/QSTitle'
import {QSText} from '../components/QSText'

export default function QuemSomos() {
	return (
		<>
			<Head>
				<title>Quem Somos | CEE</title>
			</Head>

			<Header />

			<div className={styles.container}>
				<h1>Quem Somos</h1>
			</div>

			<QSTitle />
			<QSText />
			<Footer />
		</>
	)
}
