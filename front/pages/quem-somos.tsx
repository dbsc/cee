import Head from 'next/head'
import {QSTitle} from '../components/QSTitle'
import {QSText} from '../components/QSText'

export default function QuemSomos() {
	return (
		<>
			<Head>
				<title>Quem Somos | CEE</title>
			</Head>
			<QSTitle />
			<QSText />
		</>
	)
}
