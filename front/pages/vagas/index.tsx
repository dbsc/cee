import { GetServerSideProps } from 'next'
import Head from 'next/head'
import styles from '../../styles/vagas.module.scss'
import { getSession } from 'next-auth/client'
import { CardVaga } from '../../components/CardVaga'
import { DashBoardHeader } from '../../components/DashboardHeader'
import axios from 'axios'

interface CardProps {
	id: number
	title: string
	company: string
	field: string
	position: string
	pay: string
	date: string
	location: { city: string; state: string }
}

export default function Vagas(props: [CardProps]) {
	return (
		<>
			<Head>
				<title>Vagas | CEE</title>
			</Head>

			<DashBoardHeader />
			<div className={styles.container}>
				<div className={styles.content}>
					<h1 className={styles.title}>Vagas</h1>

					<div className={styles.cards}>
						{props.map((vaga) => (
							<CardVaga
								key={vaga.id}
								id={vaga.id}
								title={vaga.title}
								company={vaga.company}
								field={vaga.field}
								position={vaga.position}
								pay={vaga.pay}
								date={vaga.date}
								location={vaga.location}
							/>
						))}
					</div>
				</div>
			</div>
		</>
	)
}

export const getServerSideProps: GetServerSideProps = async (context) => {
	const session = await getSession(context)
	if (!session) {
		return {
			redirect: {
				destination: '/',
				permanent: false,
			},
		}
	}

	const response = await axios.get(`https//localhost:8000/vacancies/vacancies/`)
	const VacancyArray = response.data.results.map((vaga) => {
		return {
			id: vaga.id,
			title: vaga.title,
			company: vaga.company.name,
			field: vaga.field,
			position: vaga.position,
			pay: new Intl.NumberFormat('pr-BR', { style: 'currency', currency: 'BRL' }).format(vaga.pay),
			date: vaga.expiration_date,
			location: vaga.location,
		}
	})

	return {
		props: VacancyArray,
	}
}
